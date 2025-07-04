
def strip_rotation(angle):
  """
    function removes unnecessary rotational moves. 
    (360 degrees is the same as 0 degrees) 
  """

  if angle >360:
    return angle % 360
  elif angle < 0:
    return 360 + angle
  else:
    return angle