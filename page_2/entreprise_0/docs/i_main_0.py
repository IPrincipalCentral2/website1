











print(f"i_hello_i .")
















<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shope</title>
  <link rel="stylesheet" href="i_style_of_work_1_i.css">
  
</head>
<body>

  <header>
    <h1> Shope </h1>
    
    <p>right here . there is a space for Entreprise</p>
    
    
    <p>i want here to run and build company very well by virtualization i</p>
    
    
  </header>

  <!-- شريط البحث -->
  <div class="search-bar">
    <input type="text" id="searchInput" placeholder="🔍 Search...">
  </div>

  <main id="projects-container" class="cards-container">
    <!-- البطاقات ستُنشأ أوتوماتيكياً هنا -->
  </main>

  <script>
    let allProjects = []; 

    fetch('i_file_of_work_1_i.json')
      .then(response => response.json())
      .then(projects => {
        allProjects = projects;
        displayProjects(allProjects);
      })
      .catch(err => console.error("Error loading topic:", err));


    function displayProjects(projects) {
      const container = document.getElementById('projects-container');
      container.innerHTML = "";

      if (projects.length === 0) {
        container.innerHTML = "<p>❌ Nothing matches your search.</p>";
        return;
      }

      projects.forEach(proj => {
        const card = document.createElement('div');
        card.className = 'card';

        card.innerHTML = `
          <div class="card-content">
            <h2>${proj.title}</h2>
            <p>${proj.description}</p>
            <div class="buttons">
              <a href="${proj.path}" target="_blank" class="btn view">📖 View</a>
              <a href="${proj.path}" download class="btn download">⬇️ Download</a>
            </div>
          </div>
        `;

        container.appendChild(card);
      });
    }

    // البحث عند الضغط على Enter
    document.getElementById("searchInput").addEventListener("keypress", function(event) 
    {
      if (event.key === "Enter") 
      {
        const keyword = event.target.value.toLowerCase();
        const filtered = allProjects.filter(proj =>
          proj.title.toLowerCase().includes(keyword) ||
          proj.description.toLowerCase().includes(keyword)
        );
        displayProjects(filtered);
      }
    });
  </script>

</body>
</html>


