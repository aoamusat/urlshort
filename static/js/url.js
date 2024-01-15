const shortURL = async function (event) {
  event.preventDefault();
  const urlInput = document.getElementById("url");
  const url = urlInput.value;

  const shortUrlElement = document.getElementById("short_url");
  const shortUrlContainer = document.getElementById("short_url_container");
  const spinner = document.getElementById("spinner");
  const submitButton = document.getElementById("submitButton");

  if (!url) {
    window.alert("Please enter a URL");

    submitButton.classList.remove("cursor-wait");
    submitButton.disabled = false;

    return;
  }

  const data = { long_url: url };

  // Show the spinner
  spinner.classList.remove("hidden");

  // disable submit button
  submitButton.disabled = true;
  submitButton.classList.add("cursor-wait");

  try {
    const response = await fetch("/api/v1/shorten", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const { short_url } = await response.json();
    shortUrlElement.textContent = `Shortened URL: ${short_url}`;
    shortUrlContainer.classList.remove("hidden");
    urlInput.value = "";
  } catch (error) {
    console.log(error.message);
    window.alert("Error: " + error.message);
  } finally {
    spinner.classList.add("hidden");
    submitButton.classList.remove("cursor-wait");
    submitButton.disabled = false;
  }
};
