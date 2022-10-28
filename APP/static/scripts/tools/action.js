
let projects = true
let types = true 
let disciplines = true
let phases = true 

let zones_area ={
    'zone_0': true,
    'area_0':true,
};

console.log(zones_area['zone_0'])
let j = 1;



document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");xw
});

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data(
        reload = projects,
        data = {},
        url = '/tools/projects',
        input_id = 'project_code',
    )
    projects = false;
})

document.getElementById('project_code').addEventListener('change',()=>{
    delete_list('types');
    delete_value('action_type')
    delete_list('disciplines');
    delete_value('discipline_code')
    delete_list('phases');
    delete_value('phase_code')
    types = true;
    disciplines = true;
    phases = true;

});

document.getElementById('action_type').addEventListener('click',()=>{
    retrive_data(
        reload = types,
        data = {},
        url = '/tools/projects',
        input_id = 'action_type',
    )
    types = false;   
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

document.getElementById('discipline_code').addEventListener('change',()=>{
    delete_list('phases');
    delete_value('phase_code')
    load_lists[disciplines] = false;  
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

document.getElementById('phase_code').addEventListener('change',()=>{});

let btns = [...document.getElementsByName('subaction_area')]

document.getElementById('more_button').addEventListener('click',() => {
    let i = j;
    zones_area[`zone_${i}`] = true;
    zones_area[`area_${i}`] = true;

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
            <datalist id="zones_${j}"></datalist>
        </div>
        <div class="dropdwn">
            <label class = "label-field">Area</label><br>
            <input class = "input-4" type="text" name = "subaction_area" id = "area_${j}">
            <datalist id="areas_${j}"></datalist>
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input class = "input-4" type="number" name = "subaction_time">
        </div>
    </div>
    `);

    document.getElementById(`zone_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = zones_area[`zone_${i}`],
            data = {},
            url = '/tools/projects',
            input_id = `zone_${i}`,
        )
        zones_area[`zone_${i}`] = false;
    })

    document.getElementById(`area_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = zones_area[`area_${i}`],
            data = {},
            url = '/tools/projects',
            input_id = `area_${i}`,
        )
        zones_area[`area_${i}`] = false;
    })
    j++;
});

document.getElementById(`zone_0`).addEventListener('click',()=>{
    retrive_data(
        reload = zones_area['zone_0'],
        data = {},
        url = '/tools/projects',
        input_id = 'area_0',
    )
    zones_area['zone_0'] = false;
})


document.getElementById(`area_0`).addEventListener('click',()=>{
    retrive_data(
        reload = zones_area['area_0'],
        data = {},
        url = '/tools/projects',
        input_id = 'area_0',
    )
    zones_area['area_0'] = false;
})