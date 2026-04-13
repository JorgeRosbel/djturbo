import math

def _distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def _detect_gesture(landmarks) -> str:
    """Detect the current gesture based on hand landmarks."""

    # finger states
    thumb_tip = landmarks.landmark[4]
    index_tip = landmarks.landmark[8]

    thumb_up = landmarks.landmark[4].y < landmarks.landmark[3].y
    index_up = landmarks.landmark[8].y < landmarks.landmark[6].y
    middle_up = landmarks.landmark[12].y < landmarks.landmark[10].y
    ring_up = landmarks.landmark[16].y < landmarks.landmark[14].y
    pinky_up = landmarks.landmark[20].y < landmarks.landmark[18].y

    distance_thumb_index = _distance(thumb_tip, index_tip)
    
    # FIST
    if not any([index_up, middle_up, ring_up, pinky_up]) and distance_thumb_index < 0.08:
        return 'fist'
    
    # SPREAD
    if all([thumb_up, index_up, middle_up, ring_up, pinky_up]):
        return 'spread'
    
    # OK
    if thumb_up and not any([middle_up, ring_up, pinky_up]) and distance_thumb_index > 0.2:
        return 'ok'

    # PINCH
    if distance_thumb_index < 0.08 and not any([middle_up, ring_up, pinky_up]):
        return 'pinch'
    

    if distance_thumb_index < 0.05:
        return "great"
    
    thumb_dir = (
    landmarks.landmark[4].x - landmarks.landmark[2].x,
    landmarks.landmark[4].y - landmarks.landmark[2].y
    )

    index_dir = (
        landmarks.landmark[8].x - landmarks.landmark[6].x,
        landmarks.landmark[8].y - landmarks.landmark[6].y
    )

    


    # cos del ángulo entre pulgar e índice para ver si es thumbs up o down
    # Cos del angulo = a * b / |a||b|
    dot = thumb_dir[0]*index_dir[0] + thumb_dir[1]*index_dir[1]
    mag1 = math.sqrt(thumb_dir[0]**2 + thumb_dir[1]**2)
    mag2 = math.sqrt(index_dir[0]**2 + index_dir[1]**2)
    cos_angle = dot / (mag1 * mag2 + 1e-6)

    # si cos cerca de 0 → ángulo cercano a 90° 

    if abs(cos_angle) < 0.3 and distance_thumb_index > 0.1:
        return "bad"

    return None


def _detect_rotation(landmarks) -> float:
    """Angle of wrist→middle_MCP vector from vertical. ~-π/2 to +π/2."""
    wrist = landmarks.landmark[0]
    mid_mcp = landmarks.landmark[9]
    dx = mid_mcp.x - wrist.x
    dy = mid_mcp.y - wrist.y
    return math.atan2(dx, -dy)  # -dy flips to: 0 = hand pointing up
