// for -> only construct in go for looping
package main

import "fmt"

func main() {
	// while looping
	// 	fmt.Println(i)
	// 	i = i + 1

	// infinte loop
	// for {
	// 	println("1")
	// }

	// 	// break
	// 	if i =2 {
	// 		continue
	// 	}
	// 	fmt.Println(i)
	// }
	//
	for i := range 11 {
		fmt.Println(i)
	}
}
