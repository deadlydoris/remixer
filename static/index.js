function mash() {
    let music_files = [];
    let track_input_1 = document.querySelector("#music_file_1");
    if (track_input_1.files.length) {
        music_files.push(track_input_1.files[0]);
    }
    let track_input_2 = document.querySelector("#music_file_2");
    if (track_input_2.files.length) {
        music_files.push(track_input_2.files[0]);
    }
    let splice_length_1 = parseFloat(document.querySelector("#splice_length_1").value);
    let splice_length_2 = parseFloat(document.querySelector("#splice_length_2").value);
    console.log(music_files);
    console.log(splice_length_1);
    console.log(splice_length_2);

    // conditional only going to execute post if we have files - only post data if spl1 and spl2 are set and #s


 
    if (music_files.length == 2 && splice_length_1 > 0 && splice_length_2 > 0) {
        var fdata = new FormData()
        fdata.append("music_file_1", music_files[0]);
        fdata.append("music_file_2", music_files[1]);
        fdata.append("splice_length_1", splice_length_1);
        fdata.append("splice_length_2", splice_length_2);

        fetch('http://localhost:8080/getmashed',
        {
                method: 'post',
                body: fdata
        }
        )}
    
}