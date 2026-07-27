import { courses } from "./data.js";

const grid = document.querySelector(".course-grid");
const loading = document.getElementById("loading");
const postsDiv = document.getElementById("posts");
const retryBtn = document.getElementById("retry-btn");

function rerender(c) {

    grid.innerHTML = "";

    c.forEach(({ code, name, credits }) => {

        const a = document.createElement("article");

        a.className = "course";

        a.dataset.name = name;
        a.dataset.credits = credits;

        a.innerHTML = `
            <h2>${name}</h2>
            <p>Code: ${code}</p>
            <p>Credits: ${credits}</p>
        `;

        grid.appendChild(a);

    });

}

const result = courses.map(
    ({ credits, name, code }) => `${code} - ${name} (${credits} credits)`
);

const result2 = courses.filter(
    ({ credits }) => credits >= 4
);

const len = result.length;

const tot_credits = courses.reduce(
    (total, { credits }) => total + credits,
    0
);

const inp = document.createElement("input");

inp.id = "search-courses";

inp.placeholder = "Search courses";

const but = document.createElement("button");

but.textContent = "SORT";

but.addEventListener("click", () => {

    const sorted = [...courses].sort(
        (a, b) => b.credits - a.credits
    );

    rerender(sorted);

});

const selectedCourse = document.createElement("div");

selectedCourse.id = "selected-course";

const p = document.createElement("p");

p.id = "total-credits";

p.textContent = `Total credits -> ${tot_credits}`;

grid.before(inp);

inp.after(but);

but.after(selectedCourse);

grid.after(p);

grid.addEventListener("click", (e) => {

    const card = e.target.closest(".course");

    if (card) {

        const name = card.dataset.name;
        const credits = card.dataset.credits;

        selectedCourse.textContent =
            `SELECTED : ${name} - ${credits}`;

        alert(`You have pressed ${name} course - ${credits} credits`);

    }

});

function rerenderfunc(val) {

    const c = courses.filter(
        ({ name }) =>
            name.toLowerCase().includes(val.toLowerCase())
    );

    rerender(c);

}

inp.addEventListener("input", () => {

    const val = inp.value;

    rerenderfunc(val);

});

function fetchUser(id) {

    return fetch("https://jsonplaceholder.typicode.com/users/" + id);

}

fetchUser(1)
    .then(response => response.json())
    .then(user => console.log(user.name));

async function fetchUserAsync(id) {

    try {

        const response = await fetch("https://jsonplaceholder.typicode.com/users/" + id);

        const user = await response.json();

        console.log(user.name);

    }

    catch (error) {

        console.log(error);

    }

}

fetchUserAsync(1);

function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        }, 1000);

    });

}

loading.textContent = "Loading courses...";

fetchAllCourses().then(data => {

    loading.textContent = "";

    rerender(data);

});

Promise.all([

    fetch("https://jsonplaceholder.typicode.com/users/1").then(r => r.json()),

    fetch("https://jsonplaceholder.typicode.com/users/2").then(r => r.json())

]).then(users => {

    console.log(users[0].name);

    console.log(users[1].name);

});

async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {

        throw new Error("Unable to load data");

    }

    return await response.json();

}

function renderPosts(posts) {

    postsDiv.innerHTML = "";

    posts.slice(0, 5).forEach(post => {

        const div = document.createElement("div");

        div.className = "post";

        div.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;

        postsDiv.appendChild(div);

    });

}

async function loadPosts() {

    loading.textContent = "Loading posts...";

    retryBtn.hidden = true;

    try {

        const posts = await apiFetch("https://jsonplaceholder.typicode.com/posts");

        loading.textContent = "";

        renderPosts(posts);

    }

    catch (error) {

        loading.textContent = "";

        postsDiv.innerHTML = "<p>Something went wrong.</p>";

        retryBtn.hidden = false;

    }

}

loadPosts();

retryBtn.addEventListener("click", loadPosts);

axios.interceptors.request.use(config => {

    console.log("API call started:", config.url);

    return config;

});

async function apiFetchAxios(url) {

    const response = await axios.get(url);

    return response.data;

}

async function loadUserPosts() {

    const response = await axios.get(
        "https://jsonplaceholder.typicode.com/posts",
        {
            params: {
                userId: 1
            }
        }
    );

    console.log(response.data);

}

loadUserPosts();

/*
Fetch vs Axios

1. Fetch requires response.json(); Axios parses JSON automatically.
2. Fetch does not throw on HTTP errors; Axios throws automatically.
3. Fetch is built into browsers; Axios is an external library with interceptors.
*/