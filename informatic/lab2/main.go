package main

import (
    "fmt"
)

func convertByte(b int) string {
    switch b {
    case 1:
        return "r1"
    case 2:
        return "r2"
    case 3:
        return "i1"
    case 4:
        return "r3"
    case 5:
        return "i2"
    case 6:
        return "i3"
    case 7:
        return "i4"
    }
    return ""
}

func main() {
    var inp string
    fmt.Scan(&inp)

    if len(inp) != 7 {
        fmt.Print("Длина сообщения должна быть 7")
        return
    }

    for _, ch := range inp {
        if ch != '1' && ch != '0' {
            fmt.Print("Строка должна состоять только из 0 или 1")
            return
        }
    }

    arr := make([]int, 7)
    for i, ch := range inp {
        arr[i] = int(ch - '0')
    }

    s1 := (arr[0] + arr[2] + arr[4] + arr[6]) % 2
    s2 := (arr[1] + arr[2] + arr[5] + arr[6]) % 2
    s3 := (arr[3] + arr[4] + arr[5] + arr[6]) % 2

    b := s3 * 4 + s2 * 2 + s1

    if b == 0 {
        fmt.Printf(
            "Правильное сообщение: %d%d%d%d\nОшибок в сообщении нет",
            arr[2],
            arr[4],
            arr[5],
            arr[6],
        )
        return
    }

    arr[b - 1] = 1 - arr[b - 1]

    fmt.Printf(
        "Правильное сообщение: %d%d%d%d\nОшибка в %d бите (%s)",
        arr[2],
        arr[4],
        arr[5],
        arr[6],
        b,
        convertByte(b),
    )
}