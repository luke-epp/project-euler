p = 1

# pythagorean triplet a^2 + b^2 = c^2 where a + b + c = 1000
best_tolerance = 100
good_a = 0
good_b = 0
good_c = 0
for (a in 1:1000){
  for (b in 1:1000){
    c = (a^2 + b^2) ^ (1/2)
    tol = abs(a + b + c -1000)
    #print(tol)
    #print(glue::glue("a :{a}, b : {b}, c: {c}"))
    if (tol < best_tolerance){
      print(glue::glue('best tolerance : {tol}'))
      good_a = a
      good_b = b
      good_c = c
      best_tolerance = tol
    }
  }
}
print(glue::glue("a :{good_a}, b : {good_b}, c: {good_c}"))
prod = good_a * good_b * good_c

print(prod)