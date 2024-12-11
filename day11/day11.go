package main

import (
	"fmt"
	"strconv"
)

var cache = make(map[string][]int)

func main() {
	fmt.Print(iterate(75))
}

func iterate(blinks int) int {
	var stones = []int{0, 44, 175060, 3442, 593, 54398, 9, 8101095}

	res := 0
	for i := 0; i < len(stones); i++ {
		res += blink(stones[i], 0, blinks)
	}

	return res
}

func checkCache(stone int, level int) int {
	stoneStr := strconv.Itoa(stone)
	if cache[stoneStr] == nil {
		cache[stoneStr] = make([]int, 75)
		return 0
	}
	return cache[stoneStr][level]
}

func setCache(stone int, level int, value int) {
	stoneStr := strconv.Itoa(stone)
	cache[stoneStr][level] = value
}

func blink(stone int, level int, maxblink int) int {

	if level == maxblink {
		return 1
	}

	cached := checkCache(stone, level)
	if cached != 0 {
		return cached
	}

	stone_count := 0
	if stone == 0 {
		stone_count = blink(1, level+1, maxblink)
	} else if len(fmt.Sprintf("%d", stone))%2 == 0 {
		stone_str := fmt.Sprintf("%d", stone)
		half_len := len(stone_str) / 2
		left, _ := strconv.Atoi(stone_str[:half_len])
		right, _ := strconv.Atoi(stone_str[half_len:])
		stone_count += blink(left, level+1, maxblink)
		stone_count += blink(right, level+1, maxblink)
	} else {
		stone_count += blink(stone*2024, level+1, maxblink)
	}

	setCache(stone, level, stone_count)

	return stone_count

}
