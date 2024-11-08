function setTriangleHeight() {
  const top_triangle = document.getElementById("top-triangles");
  const bottom_triangle = document.getElementById("bottom-triangle");
  const width = top_triangle.offsetWidth;

  top_triangle.style.height = width * 0.2 + "px";
  bottom_triangle.style.height = width * 0.2 + "px";
}

window.addEventListener("load", setTriangleHeight);

window.addEventListener("resize", setTriangleHeight);
