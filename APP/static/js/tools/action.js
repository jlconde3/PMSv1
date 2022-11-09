let j = 1;

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/tools/projects',
        input_id = 'project_code',
        id_list = ['discipline_code','phase_code'],
        name_list = []
    )
});

document.getElementById('discipline_code').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project_code:document.getElementById('project_code').value},
        url = '/tools/disciplines',
        input_id = 'discipline_code',
        id_list = ['phase_code'],
        name_list = []
    )
});

document.getElementById('phase_code').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project_code:document.getElementById('project_code').value,
            discipline_code:document.getElementById('discipline_code').value,
        },
        url = '/tools/phases',
        input_id = 'phase_code',
        id_list = [],
        name_list = []
    )
});

document.getElementById('action_type').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project_code: document.getElementById('project_code').value,
            discipline_code: document.getElementById('discipline_code').value,
        },
        url = '/tools/actions_stations',
        input_id = 'action_type',
        id_list = [],
        name_list = []
    )
});

document.getElementById(`zone_0`).addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value
        },
        url = '/tools/zones',
        input_id = 'zone_0',
        id_list = [],
        name_list = []
    )
});

document.getElementById(`area_0`).addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value,
            'zone_code':document.getElementById('zone_0').value
        },
        url = '/tools/areas',
        input_id = 'area_0',
        id_list = [],
        name_list = []
    )
});

document.getElementById('more_button').addEventListener('click',() => {
    let i = j;

    add_more('subactions',
    `
    <div>
        <label class = "label-title">Subaction</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">Custom code</label><br>
            <input class = "input-4" type="text" name = "custom_code">
        </div>
        <div class="dropdwn">
            <label class = "label-field">Zone</label><br>
            <input class = "input-4" type="text" name = "subaction_zone" id = "zone_${j}">
            <datalist id="zones_${j}" class = "input-4"></datalist>
        </div>
        <div class="dropdwn">
            <label class = "label-field">Area</label><br>
            <input class = "input-4" type="text" name = "subaction_area" id = "area_${j}">
            <datalist id="areas_${j}" class = "input-4" ></datalist>
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input class = "input-4" type="number" name = "subaction_time">
        </div>
    </div>
    `);

    document.getElementById(`zone_${i}`).addEventListener('click',()=>{
        retrive_data_actions(
            data = {
                'project_code': document.getElementById('project_code').value,
                'discipline_code': document.getElementById('discipline_code').value,
                'phase_code':document.getElementById('phase_code').value,
            },
            url = '/tools/zones',
            input_id = `zone_${i}`,
            id_list = [],
            name_list = []
        )
    })

    document.getElementById(`area_${i}`).addEventListener('click',()=>{
        retrive_data_actions(
            data = {
                'project_code': document.getElementById('project_code').value,
                'discipline_code': document.getElementById('discipline_code').value,
                'phase_code':document.getElementById('phase_code').value,
                'zone_code':document.getElementById(`zone_${i}`).value
            },
            url = '/tools/areas',
            input_id = `area_${i}`,
            id_list = [],
            name_list = []
        )
    })
    j++;
});



document.getElementById('submit_button').addEventListener('click',() => {
    let i = 0;
    let empty = false;
    const inputs = document.getElementsByTagName('input');
    
    for (input of inputs){
        if (input.value.replace(/ /g,'') == ""){
            input.style.border = "red solid 1px";
            empty = true;
        }
        else{
            input.style.border = "#EAEAEA solid 1px";
        }
        i++;
    }
    console.log(empty)

    if (!empty){        
        let data = {
            project_code: element_id_value('project_code'),
            customer_code: element_id_value('customer_code'),
            action_type: element_id_value('action_type'),
            action_date: element_id_value('action_date'),
            discipline_code:element_id_value('discipline_code'),
            phase_code: element_id_value('phase_code'),
            action_description: element_id_value('action_description'),
            custom_code: element_name_value('custom_code'),
            subaction_zone: element_name_value('subaction_zone'),
            subaction_area: element_name_value('subaction_area'),
            subaction_time: element_name_value('subaction_time')
        };
        fetch('/tools/create_action', {
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json'
            }
        }).then(
            window.location.replace("/tools")
        )
    }
    else{
        alert("You left some fields empty!!")
    }
});

document.getElementById('action_description').addEventListener('keyup',()=>{
    var characterCount = document.getElementById('action_description').value.length;
    current = document.getElementById('current');
    current.innerText = characterCount;

});