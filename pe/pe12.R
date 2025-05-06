source('/Users/lukeepp/project-euler/pe/utils.R')
current.triangle = 0
for (i in 1:1000000) {
  current.triangle = current.triangle + i
  num.divs = length(GetDivisors(current.triangle))
  if (num.divs > 500) {
    message(current.triangle)
    break
  }
}
