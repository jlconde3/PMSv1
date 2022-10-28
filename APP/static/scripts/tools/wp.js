let j = 1;
let q = 1;

let projects = true;
let disciplines = true;
let phases = true;
let zones = true;
let types = true;
let stations = true;


let action_area_task ={
    'actions_0':true,
    'areas_0': true,
    'tasks_0':true,
    'users_0':true,
};

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
  }

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data(
        reload = projects,
        data = {},
        url = '/tools/projects',
        input_id = 'project_code',
    )
    projects = false;
});

document.getElementById('discipline_code').addEventListener('click',()=>{
    retrive_data(
        reload = disciplines,
        data = {},
        url = '/tools/projects',
        input_id = 'discipline_code',
    )
    disciplines = false;   
});

document.getElementById('phase_code').addEventListener('click',()=>{
    retrive_data(
        reload = phases,
        data = {},
        url = '/tools/projects',
        input_id = 'phase_code',
    )
    phases = false;   
});

document.getElementById('wp_zone').addEventListener('click',()=>{
    retrive_data(
        reload = zones,
        data = {},
        url = '/tools/projects',
        input_id = 'wp_zone',
    )
    zones = false;   
});

document.getElementById('wp_type').addEventListener('click',()=>{
    retrive_data(
        reload = types,
        data = {},
        url = '/tools/projects',
        input_id = 'wp_type',
    )
    types = false;   
});

document.getElementById('wp_station').addEventListener('click',()=>{
    retrive_data(
        reload = stations,
        data = {},
        url = '/tools/projects',
        input_id = 'wp_station',
    )
    stations = false;   
});

document.getElementById(`action_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`actions_0`],
        data = {},
        url = '/tools/projects',
        input_id = `action_0`,
    )
    action_area_task[`actions_0`] = false;
})
document.getElementById(`area_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`areas_0`],
        data = {},
        url = '/tools/projects',
        input_id = `area_0`,
    )
    action_area_task[`area_0`] = false;
})

document.getElementById(`task_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`tasks_0`],
        data = {},
        url = '/tools/projects',
        input_id = `task_0`,
    )
    action_area_task[`tasks_0`] = false;
})


document.getElementById('more_button').addEventListener('click',() => {
    let i = j;
    action_area_task[`actions_${i}`] = true;
    action_area_task[`areas_${i}`] = true;
    action_area_task[`tasks_${i}`] = true;

    add_more('subtasks',
    `
    <div>
        <label class = "label-title">Task</label>
    </div>
    <div class="fields-group">
    <div>
        <label class = "label-field">Action</label><br>
        <input class = "input-3" name = "task_action" list="actions" id="action_${i}">
        <datalist id="actions_${i}" class = "input-3" ></datalist>
    </div>
    <div>
        <label class = "label-field">Area</label><br>
        <input class = "input-3" type="text" name = "task_area" id="area_${i}">
        <datalist id="areas_${i}" class = "input-3"></datalist>
    </div>
    <div>
        <label class = "label-field">Task</label><br>
        <input class = "input-3" name = "task_code" id="task_${i}">
        <datalist id="tasks_${i}" class = "input-3"></datalist>
    </div>
    </div>
    `);

    document.getElementById(`action_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`actions_${i}`],
            data = {},
            url = '/tools/projects',
            input_id = `action_${i}`,
        )
        action_area_task[`actions_${i}`] = false;
    });
    document.getElementById(`area_${j}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`areas_${i}`],
            data = {},
            url = '/tools/projects',
            input_id = `area_${i}`,
        )
        action_area_task[`areas_${i}`] = false;
    });
    document.getElementById(`task_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`tasks_${i}`],
            data = {},
            url = '/tools/projects',
            input_id = `task_${i}`,
        )
        action_area_task[`tasks_${i}`] = false;
    });
    j++;
});



document.getElementById('submit_button').addEventListener('click',() => {
    document.body.style.overflow = "hidden"
    document.getElementById('validate_window').showModal();
});

document.getElementById(`user_0`).addEventListener('click',()=>{
    console.log("Hola")
    retrive_data(
        reload = action_area_task[`users_0`],
        data = {},
        url = '/tools/projects',
        input_id = `user_0`,
    )
    action_area_task[`users_0`] = false;
});

document.getElementById('more_users_button').addEventListener('click',() => {
    let k = q;
    action_area_task[`users_${k}`] = true;
    add_more('users',
    `
    <div>
        <label class = "label-title">In charge</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">User</label><br>
            <input type="text" name = "username" id = "user_${k}">
            <datalist class = "input-4" id="users_${k}" ></datalist>
        </div>
        <div>
            <label class = "label-field">Level</label><br>
            <input type="number" name = "user_level" id = "user_level_${k}">
        </div>
    </div>
    `);

    document.getElementById(`user_${k}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`users_${k}`],
            data = {},
            url = '/tools/projects',
            input_id = `user_${k}`,
        )
        action_area_task[`users_${k}`] = false;
    });
    q++;
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
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







