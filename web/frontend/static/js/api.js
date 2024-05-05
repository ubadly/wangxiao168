function get_request(url) {
    return new Promise((resolve, reject) => {
        fetch(url).then(res => res.json()).then(
            resolve(res)
        )
    })
}


function post_request(url, data) {
    let formData = new FormData();
    Object.keys(data).forEach((key) => {
        formData.append(key, data[key]);
    })

    return new Promise((resolve, reject) => {
        fetch(url, {
            method: 'POST',
            body:formData
        }).then(res => res.json()).then(
            res => resolve(res)
        )
    })
}