








content_of_research_of_word_in_a_file_0 = r"""


<script>
  // دالة البحث
  async function searchProjects(keyword) {
    try {
      // جلب البيانات من الملف JSON
      const response = await fetch('file_1.json');
      const projects = await response.json();

      // فلترة العناصر التي تحتوي الكلمة
      const results = projects.filter(proj =>
        proj.title.includes(keyword) || proj.description.includes(keyword)
      );

      return results;
    } catch (err) {
      console.error("خطأ أثناء البحث:", err);
      return [];
    }
  }

  // تجربة الدالة
  searchProjects("الدكتوراه").then(results => {
    console.log("نتائج البحث:", results);
  });
</script>



"""











