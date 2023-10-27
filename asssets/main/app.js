var DescripText630ScreenBelow = `At Living Plus Care Service, we believe in the power of choice. We understand 
that every individaul is unique, and so are their needs. WE ARE HERE TO HELP.`;

var DescripText550ScreenBelow = `At Living Plus Care Service, we believe in the power of choice. WE ARE HERE TO HELP.`;


var description = document.getElementById('home-page-text-description');
 
var sw = screen.width;

if (sw <= 630) {
	description.innerHTML = DescripText630ScreenBelow;
	
	console.log(description)
}

if (sw <= 550) {
	description.innerHTML = DescripText550ScreenBelow;
	console.log(description)
}




// run after page loads
function change_p_innerHTML(argument) {
	// change the innerHTML of a p tag based on screen size
}