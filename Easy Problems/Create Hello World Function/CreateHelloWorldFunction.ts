function createHelloWorld() {
    
	return function(...args): string {
			//just return hello world lol
			
			return "Hello World"
	};
};

/**
* const f = createHelloWorld();
* f(); // "Hello World"
*/