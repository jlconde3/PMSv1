let j = 1;

//Template for tasks
const task_template = ` 
    <div>
        <label class = "label-title">Task</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">Action</label><br>
            <input class = "input-3" name = "task_action" list="actions" id="action_${j}>
            <datalist id="actions_${j}" class = "input-3" ></datalist>
        </div>
        <div>
            <label class = "label-field">Area</label><br>
            <input class = "input-3" type="text" name = "task_area" id="area_${j}>
            <datalist id="areas_${j}" class = "input-3"></datalist>
        </div>
        <div>
            <label class = "label-field">Task</label><br>
            <input class = "input-3" name = "task_code" id="task_${j}>
            <datalist id="tasks_${j}" class = "input-3"></datalist>
        </div>
    </div>
`;

const user_template =`
    <div>
        <label class = "label-title">In charge</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">User</label><br>
            <input type="text" name = "username" list = "users_list">
        </div>
        <div>
            <label class = "label-field">Level</label><br>
            <input type="number" name = "user_level">
        </div>
    </div>
`;

document.getElementById('more_button').addEventListener('click',() => {
    add_more('subactions',task_template);
});

document.getElementById('submit_button').addEventListener('click',() => {
    document.body.style.overflow = "hidden"
    document.getElementById('validate_window').showModal();
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('more_users_button').addEventListener('click',() => {
    add_more( 'users',user_template);
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
        username: element_name_value('username'),
        user_level: element_name_value('user_level')
    };
    
    fetch('/tools/create_wp', {
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(window.location.replace("/tools"));
});

document.getElementById('cancel_validate_button').addEventListener('click',() => {
    document.body.style.overflow = "visible"
    document.getElementById('validate_window').close(); 
});







