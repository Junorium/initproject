async function search() {
    const query = document.getElementById('query').value;
    const res = await fetch(`http://localhost:5000/api/news?q=${query}`);
    const data = await res.json();

    const results = document.getElementById('results');
    results.innerHTML = '';
    data.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item.title;
        results.appendChild(li);
    })
}
