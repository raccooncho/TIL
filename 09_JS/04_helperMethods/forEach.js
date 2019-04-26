// ES5 for loop
var colors = ['red', 'blue', 'green'];
for (var i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}



// ES6+
const Colors = ['red', 'blue', 'green'];
Colors.forEach(color =>{
    console.log(color)
});

function handlePosts() {
    const posts = [
    {id: 23, title: 'Daily js news'},
    {id: 24, title: 'Daily python news'},
    {id: 25, title: 'Daily juby news'},
    {id: 26, title: 'Daily Django news'},
    ];
    posts.forEach(post => {
        savePost(post);
    })
}
