let elem = document.getElementById("cont");
let inp = elem.getElementsByTagName("input");

let cur_elem = 0;

setInterval(switch_button, 7000);


function switch_button(){
	
	if (cur_elem == 2){cur_elem = -1};
	cur_elem++;
	inp[cur_elem].checked = true;
	
}