const CRYSTAL_SIZE = 500;
const SIDES = 6;
let PALETTE = [];

function setup() {
  createCanvas(530, 530, SVG);

  PALETTE = [
    color(255, 52, 154), // pink
    color(4, 0, 152)    // blue
  ];

  noLoop();
  angleMode(DEGREES);
  rectMode(CENTER);

  // Add a mouse click event listener to the canvas
  canvas.mouseClicked(restartDraw);
}

function draw() {
  background(255); // Clear the background

  const circles = new Circles();
  circles.render();

  const simpleLines = new SimpleLines();
  simpleLines.render();

  const outlineShape = new OutlineShape();
  outlineShape.render();

  //testLines();
}

// Call the draw function every 2 seconds (2000 milliseconds)
setInterval(draw, 500);

// Function to restart the draw loop on mouse click
function restartDraw() {
  loop(); // Start the loop
}
