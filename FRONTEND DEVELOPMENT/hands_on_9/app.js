import { courses } from "./data.js";

const grid = document.querySelector(".course-grid");
const search = document.getElementById("search-courses");
const sortBtn = document.getElementById("sort-btn");
const results = document.getElementById("results-count");
const postsDiv = document.getElementById("posts");
const retryBtn = document.getElementById("retry-btn");
const menuBtn = document.getElementById("menu-btn");

function renderCourses(courseList) {

    grid.innerHTML = "";

    results.textContent = `${courseList.length} courses found`;

    courseList.forEach(({ code, name, credits }) => {

        const card = document.createElement("article");

        card.className = "course";

        card.tabIndex = 0;

        card.setAttribute("role", "button");

        card.setAttribute(
            "aria-label",
            `${name}, ${credits} credits`
        );

        card.innerHTML = `
            <h2>${name}</h2>
            <p>Code: ${code}</p>
            <p>Credits: ${credits}</p>
        `;

        card.addEventListener("click", () => {

            alert(`${name} selected`);

        });

        card.addEventListener("keydown", (e) => {

            if (e.key === "Enter") {

                card.click();

            }

        });

        grid.appendChild(card);

    });

}

renderCourses(courses);

search.addEventListener("input", () => {

    const value = search.value.toLowerCase();

    const filtered = courses.filter(course =>
        course.name.toLowerCase().includes(value)
    );

    renderCourses(filtered);

});

sortBtn.addEventListener("click", () => {

    const sorted = [...courses].sort(
        (a, b) => b.credits - a.credits
    );

    renderCourses(sorted);

});

menuBtn.addEventListener("click", () => {

    const expanded =
        menuBtn.getAttribute("aria-expanded") === "true";

    menuBtn.setAttribute(
        "aria-expanded",
        !expanded
    );

});

function fetchUser(id) {

    return fetch(
        "https://jsonplaceholder.typicode.com/users/" + id
    );

}

fetchUser(1)
.then(response => response.json())
.then(user => console.log(user.name));

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users/" + id
        );

        const user = await response.json();

        console.log(user.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(1);

function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        },1000);

    });

}

fetchAllCourses().then(data => {

    renderCourses(data);

});

Promise.all([

    fetch("https://jsonplaceholder.typicode.com/users/1")
    .then(r=>r.json()),

    fetch("https://jsonplaceholder.typicode.com/users/2")
    .then(r=>r.json())

]).then(users=>{

    console.log(users[0].name);

    console.log(users[1].name);

});

async function apiFetch(url){

    const response = await fetch(url);

    if(!response.ok){

        throw new Error("Unable to load data");

    }

    return await response.json();

}

function renderPosts(posts){

    postsDiv.innerHTML="";

    posts.slice(0,5).forEach(post=>{

        const div=document.createElement("div");

        div.className="post";

        div.innerHTML=`
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;

        postsDiv.appendChild(div);

    });

}

async function loadPosts(){

    retryBtn.hidden=true;

    try{

        const posts = await apiFetch(
            "https://jsonplaceholder.typicode.com/posts"
        );

        renderPosts(posts);

    }

    catch(error){

        postsDiv.innerHTML="<p>Unable to load notifications.</p>";

        retryBtn.hidden=false;

    }

}

loadPosts();

retryBtn.addEventListener("click",loadPosts);

axios.interceptors.request.use(config=>{

    console.log("API call started:",config.url);

    return config;

});

async function apiFetchAxios(url){

    const response = await axios.get(url);

    return response.data;

}

async function loadUserPosts(){

    const response = await axios.get(

        "https://jsonplaceholder.typicode.com/posts",

        {

            params:{

                userId:1

            }

        }

    );

    console.log(response.data);

}

loadUserPosts();

if(!window.CSS || !CSS.supports("display","grid")){

    console.log("CSS Grid not supported.");

}

/*
Fetch vs Axios

1. Fetch needs response.json(); Axios parses JSON automatically.

2. Fetch doesn't throw on HTTP errors.
Axios throws automatically.

3. Fetch is built into browsers.
Axios supports interceptors and timeout.
*/