from sage.all import sqrt, floor, ZZ

def main():
    cnt = 0
    for n in range(1, 50):
        done = false
        for t in range(1, 100000):
            D = t * (t + 1)
            N = 16*n - t * (t + 1)

            u = 2*t + 1 + 2 * sqrt(t*(t+1))

            xbound = sqrt(abs(N)) * (1 + sqrt(u)) / 2
            ybound = sqrt(abs(N)) * (1 + sqrt(u)) / (2 * sqrt(D))

            xint = floor(abs(xbound))
            yint = floor(abs(ybound))


            for y in range(1, int(yint) + 1, 2):
                c = N + D * y * y
                if c.is_square():
                    cnt += 1
                    print(c, y, t, "value of n:", n)
                    done = true
                    break
            if done:
                break

if __name__ == "__main__":
    main()
