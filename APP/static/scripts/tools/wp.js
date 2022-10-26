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
    document.getElementById('validate_window').showModal();
});
document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools")
});

document.getElementById('validate_button').addEventListener('click',() => {
    let data = {
        project_code: element_id_value('project_code'),
        discipline_code: element_id_value('discipline_code'),
        phase_code: element_id_value('phase_code'),
        wp_type: element_id_value('wp_station'),
        wp_station: element_id_value('wp_station'),
        wp_zone: element_id_value('wp_zone'),
        task_action: element_name_value('task_action'),
        task_area: element_name_value('task_area'),
        task_code: element_name_value('task_code'),
        wp_code: element_id_value('wp_code'),
        wp_difficulty: element_id_value('wp_difficulty'),
        wp_volume: element_id_value('wp_volume'),
        wp_complexity: element_id_value('wp_complexity'),
        wp_contracted_time: element_id_value('wp_contracted_time'),
        wp_planned_time: element_id_value('wp_planned_time'),
        wp_scheduled_time:  element_id_value('wp_scheduled_time'),
    };
    
    fetch('/tools/create_wp', {
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(window.location.replace("/tools"))
});

document.getElementById('cancel_validate_button').addEventListener('click',() => {
    document.getElementById('validate_window').close(); 
});







