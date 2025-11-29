const date = new Date();
document.querySelectorAll('.room-btn').forEach(roomBtn => {
    roomBtn.dataset.room
});

//$(document).ready(function() {
    $('.room-btn').click(function() {
        // get room number
        let room_id = this.innerHTML;

        // MODIFY MODAL CONTENT
        // insert room id
        let rid_disp = document.getElementById("room_id");
        rid_disp.setAttribute('value', room_id);
        rid_disp.setAttribute('readonly', true);

        // insert date
        let date_disp = document.getElementById("date"); // get the date from the calendar somehow
        date_disp.setAttribute('value', `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`);
        date_disp.setAttribute('readonly', true);
    });

    // $('.date-selector').click(function() {
    //     // added by mat taylor (can delete when needed)
    //     // remove the 'current-date' class to the div that it was previously on
    //     let calender_days_disp = document.querySelector('/'.calendar-days);
    //     console.log(calender_days_disp.children.length);
        
    //     for (let i=0; i<31; i++); {
    //         let day_disp = calender_days_disp.children[i]
    //         console.log(day_disp);
    //         day_disp.classList.remove('current-date');
    //     }
    //     // add the 'current-date' class to 'this'
    //     this.classList.add('current-date');
    // });

    export function addAvailableRoomButtons(rooms) {
	let available_rooms_disp = document.getElementById("rooms-available");
	available_rooms_disp.innerHTML = "";
	// make a button for each available room
	for (let i=0; i<rooms.length; i++) {
	    let room_btn = document.createElement("button");
	    room_btn.innerHTML = rooms[i];

	    room_btn.classList.add("room-btn");
            room_btn.classList.add("btn");
	    room_btn.classList.add("btn-outline-primary");

	    room_btn.setAttribute('for', rooms[i]);
	    room_btn.setAttribute('data-bs-toggle', 'modal');
	    room_btn.setAttribute('data-bs-target', '#exampleModal');
	    
	    room_btn.addEventListener("click", function() {
		// get room number
        	let room_id = this.innerHTML;

	        // MODIFY MODAL CONTENT
        	// insert room id
                let rid_disp = document.getElementById("room_id");
        	rid_disp.setAttribute('value', room_id);
        	rid_disp.setAttribute('readonly', true);

	        // insert date
        	let date_disp = document.getElementById("date"); // get the date from the calendar somehow
        	date_disp.setAttribute('value', `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`);
        	date_disp.setAttribute('readonly', true);
	    });

	    available_rooms_disp.appendChild(room_btn);
	}
    }
//});