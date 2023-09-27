package main

type Engine struct {
	cylinder int
}

func NewEngine(cylinder int) Engine {
	engine := Engine{cylinder: cylinder}
	return engine
}

type Car struct {
	model  int
	name   string
	engine Engine
}

func main() {
	engine := NewEngine(10)
	car := Car{}
	car.model = 10
	car.name = "Ford"
	car.engine = engine
	_ = car
}
