import { courses } from "./data.js";

function rerender(c){

    grid.innerHTML="";

    c.forEach(({code , name , credits})=>{

        const a=document.createElement("article");

        a.className="course";

        // Added for event delegation
        a.dataset.name = name;
        a.dataset.credits = credits;

        a.innerHTML=`
            <h2>${name}</h2>
            <p>Code: ${code}</p>
            <p>Credits: ${credits}</p>
        `;

        grid.appendChild(a);
    })

}


const result = courses.map(
    ({credits , name , code}) => `${code} - ${name} (${credits} credits)`
);


const result2 = courses.filter(
    ({credits}) => credits >= 4
);


const len = result.length;


// reduce combines all elements into single value
const tot_credits = courses.reduce(
    (total , {credits}) => total + credits, 
    0
);


const inp=document.createElement("input");

inp.id="search-courses";

inp.placeholder="Search courses";


// adding button
const but=document.createElement("button");

but.textContent="SORT";


// sort courses by credits(desc)
but.addEventListener("click",()=>{

    const sorted=[...courses].sort(
        (a,b)=> b.credits - a.credits
    );

    rerender(sorted);

});


// creating selected course div
const selectedCourse=document.createElement("div");

selectedCourse.id="selected-course";

but.after(selectedCourse);



const grid=document.querySelector(".course-grid");

grid.before(inp);

inp.after(but);


// EVENT DELEGATION ADDED HERE

grid.addEventListener("click",(e)=>{

    const card=e.target.closest(".course");

    if(card){

        const name=card.dataset.name;
        const credits=card.dataset.credits;

        selectedCourse.textContent =
        `SELECTED : ${name} - ${credits}`;

        alert(`You have pressed ${name} course - ${credits} credits`);
    }

});



rerender(courses);



// total credits display
const p=document.createElement("p");

p.id="total-credits";

p.textContent=`Total credits -> ${tot_credits}`;

grid.after(p);



function rerenderfunc(val){

    const c=courses.filter(
        ({name}) => 
        name.toLowerCase().includes(val.toLowerCase())
    );

    rerender(c);

}



// search event
inp.addEventListener("input",()=>{

    const val=inp.value;

    rerenderfunc(val);

});