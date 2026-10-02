package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	var cc string
	fmt.Scan(&cc)

	if cc == "10" {
		var a int
		fmt.Scan(&a)

		res := ""

		i := 2
		p := a
		for p > 0 {
			res = fmt.Sprintf("%d", p%i) + res
			p /= i
			i++
		}

		fmt.Println(res)
	} else if strings.ToLower(cc) == "фиб" {
		var a string
		fmt.Scan(&a)

		for i := 0; i < len(a)-1; i++ {
			if a[i] == '1' && a[i+1] == '1' {
				fmt.Println("В числе фибоначи не может быть двух подряд идущих единиц")
				return
			}
		}

		n := len(a)

		dp := make([]int, n+2)
		dp[0] = 1
		dp[1] = 1
		for i := 2; i <= n+1; i++ {
			dp[i] = dp[i-2] + dp[i-1]
		}

		res := 0
		for i := 0; i < n; i++ {
			res += dp[n-i] * (int(a[i]) - '0')
		}

		fmt.Println(res)
	} else if strings.ToLower(cc) == "берг" {
		var a string
		fmt.Scan(&a)

		n := len(a)
		m := len(strings.Split(a, ".")[0])

		res := 0.0
		f := 0
		for i := 0; i < n; i++ {
			if a[i] == '.' {
				f = 1
				continue
			}

			res += math.Pow((1+math.Sqrt(5))/2, float64(n-m-i+f-1)) * float64((int(a[i]) - '0'))
		}

		fmt.Println(res)
	} else if strings.ToLower(cc) == "13c" {
		var a string
		fmt.Scan(&a)

		a = strings.Replace(a, "{", "", -1)
		a = strings.Replace(a, "}", "", -1)

		n := len(a)
		k := strings.Count(a, "^")
		kk := 0

		res := 0.0
		f := false

		for i := 0; i < n; i++ {
			if a[i] == '^' {
				f = true
				kk++
				continue
			}

			h := float64(a[i] - '0')

			if f {
				h = -h
			}

			f = false

			res += h * math.Pow(13, float64(n-k+kk-i-1))
		}

		fmt.Println(res)
	}
}
