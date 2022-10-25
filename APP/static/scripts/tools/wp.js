//Var for number the tasks
let n = 1; 

//Template for tasks
let task_template = ` 
    <div>
        <label class = "label-title">Task</label>
        </div>
        <div class="fields-group">
        <div>
            <label class = "label-field">Action</label><br>
            <input class = "input-3" id = "zone_code">
        </div>
        <div>
            <label class = "label-field">Area</label><br>
            <input class = "input-3" type="text" id = "phase_code">
        </div>
        <div>
            <label class = "label-field">Task</label><br>
            <input class = "input-3" id = "zone_code">
        </div>
    </div>
`;

document.getElementById('more_button').addEventListener('click',() => 
    add_more( 'tasks',`task_${n}`,task_template)
);

document.getElementById('submit_button').addEventListener('click',() => {
    document.getElementById('main').setAttribute('style','filter:blur(4px)')
    document.getElementById('validate_window').showModal();
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools")
});

document.getElementById('validate_button').addEventListener('click',() => {
    window.location.replace("/tools")
});

document.getElementById('cancel_validate_button').addEventListener('click',() => {
    document.getElementById('main').setAttribute('style','filter:none')
    document.getElementById('validate-window').close(); 
});



