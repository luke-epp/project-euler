GetDivisors = function(n) {
  low = 1:floor(sqrt(n))
  divs = low[n %% low == 0]
  c(divs, n / divs[n / divs != divs]) |> sort()
}
# tests
test1 = GetDivisors(2) == c(1, 2)
stopifnot(test1)
GetDivisors(27)


Collat = function(n) {
  if (n %% 2 == 0) {
    return(n / 2)
  } else {
    return(3 * n + 1)
  }
}
