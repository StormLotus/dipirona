class Bubble {
	constructor(x, y, r) {
		this.x = x;
		this.y = y;
		this.r = r;
		this.brightness = 0;
	}

	clicked(px, py) {
		let d = dist(px, py, this.x, this.y);
		if (d < this.r) {
			this.brightness = 255;
		}
	}

	move() {
		this.x = this.x + random(-2, 2);
		this.y = this.y + random(-2, 2);
	}

	show() {
		stroke(255);
		strokeWeight(4);
		fill(this.brightness, 125);
		ellipse(this.x, this.y, this.r * 2);
	}
}