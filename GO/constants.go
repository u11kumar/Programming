package main

import "fmt"

const age = 30

// short-hand is not allowed outside the function

func main() {
	// :=
	// const name = "golang"
	// const age =30
	fmt.Println(age)

	const (
		port = 5500
		host = "localhost"
	)

	fmt.Println(port, host)
}
