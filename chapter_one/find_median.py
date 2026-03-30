def get_median_font_size(font_sizes):
   sorted_sizes = sorted(font_sizes)
   return(
      None if not sorted_sizes 
      else sorted_sizes[(len(sorted_sizes)-1)//2]
   )

