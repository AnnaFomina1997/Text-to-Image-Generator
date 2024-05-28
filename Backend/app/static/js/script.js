document.getElementById("textForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const inputText = document.getElementById("inputText").value;

    // Показать индикатор загрузки
    const loadingIndicator = document.getElementById("loading");
    loadingIndicator.style.display = 'inline-block';

    try {
        const response = await fetch('http://localhost:8001/generate-image/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });

        if (response.ok) {
            const data = await response.json();
            const imagePath = data.image_path;

            const generatedImage = document.getElementById("generatedImage");
            generatedImage.src = 'http://localhost:8001/' + imagePath + '?' + new Date().getTime(); // Добавление параметра времени для предотвращения кэширования
            generatedImage.style.display = 'block';
        } else {
            console.error('Error generating image:', response.statusText);
        }
    } catch (error) {
        console.error('Network error:', error);
    } finally {
        // Скрыть индикатор загрузки
        loadingIndicator.style.display = 'none';
    }
});
