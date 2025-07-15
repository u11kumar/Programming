package main

import "fmt"

func main() {
	var age int = 18
	if age >= 18 {
		fmt.Println("Person is an adult")
	} else {
		fmt.Println("Person is not an adult")
	}
	age = 10
	if age >= 18 {
		fmt.Println("Person is an adult")
	} else if age >= 12 {
		fmt.Println("Person is a teenager")
	} else {
		fmt.Println("Person is a kid")
	}

	role := "admin"
	hasPermission := false
	if role == "admin" || hasPermission {
		fmt.Println("yes")
	}

	if age=20;age=18{
		fmt.Println("Person is an adult.",age)
	} else if age>=12{
		fmt.Println("Person ia a teenager",age)
	}

	
	// go lang goes not have a  ternary operator
	// You have to use normal if else
}
