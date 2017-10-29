function preload() {
	// Load data.
	table = loadTable(dados, "csv", "header");
}

let people = []

function setup() {
	// Plot graph.
	createCanvas(300, 300);
	background(255);
	translate(width/2, height/2);

	let x, y, theta, r, alphas = table.getColumn("alpha"), ids = table.getColumn("ID Name");
	for (let i = 0; i < table.getRowCount(); i++) {
		theta = random(360);
		r = map(alphas[i], 0, 1, 0, 180);

		x = r * cos(theta);
		y = r * sin(theta);

		ellipseMode(CENTER);
		noStroke();
		fill(0);
		ellipse(x, y, 10, 10);

		let p = new Bubble(x, y, ids[i]);
		people.push(p);
	}
}

function draw() {
	for (let i = 0; i < people.length; i++) {
		people[i].rollover(mouseX, mouseY);
	}
}

class Bubble {
	constructor(x, y, id) {
		this.x = x;
		this.y = y;
		this.r = 10;
		this.id = id;
		this.brightness = 0;
	}
	
	rollover(px, py) {
		let d = dist(px, py, this.x, this.y);
		if (d < this.r) {
			this.brightness = 255;
			console.log("Now on " + this.id);
		} else {
			this.brightness = 0;
		}
	}
}