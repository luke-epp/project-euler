source('/Users/lukeepp/project-euler/pe/utils.R')
max.counter = -Inf
for (i in 1:10^6) {
  cur.num = i
  cur.counter = 0
  while (cur.num != 1) {
    cur.num = Collat(cur.num)
    cur.counter = cur.counter + 1
  }
  if (cur.counter > max.counter) {
    max.counter = cur.counter
    max.number = i
  }
}
print(max.number)
