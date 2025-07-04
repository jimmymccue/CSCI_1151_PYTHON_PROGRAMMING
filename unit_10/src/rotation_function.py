
def strip_rotation(angle: int):
  """
    function removes unnecessary rotational moves. 
    (360 degrees is the same as 0 degrees) 
  """

  try:
      if not isinstance(angle, int):            #I was not sureof this logic so I got a 
        raise TypeError("Non Numeric Number")   #little help from AI. Still not sure but
                                                #it does work now
  except TypeError:
      return "You must enter a numeric value"
  
  else:
    if angle > 360 or angle < 0:
      return angle % 360
    else:
      return angle