<<<<<<< HEAD
function checkSubmit(){
	var a=document.getElementById("password");
	if("undefined"!=typeof a){
		if("bd8e01b5a292d65a137d0f1fd3d4a7c5"==a.value)
			return!0;
			alert("Error");
			a.focus();
			return!1
		}
	}

=======
function checkSubmit(){
	var a=document.getElementById("password");
	if("undefined"!=typeof a){
		if("bd8e01b5a292d65a137d0f1fd3d4a7c5"==a.value)
			return!0;
			alert("Error");
			a.focus();
			return!1
		}
	}

>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
document.getElementById("levelQuest").onsubmit=checkSubmit;';