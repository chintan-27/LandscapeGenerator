function hexToRgb(hex) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result
    ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16),
      }
    : null;
}

async function submit() {
  let colorpicker1 = document.getElementById("colorPicker1");
  let colorpicker2 = document.getElementById("colorPicker2");
  let colorpicker3 = document.getElementById("colorPicker3");
  let colorpicker4 = document.getElementById("colorPicker4");
  let colorpicker5 = document.getElementById("colorPicker5");
  let colors = [];
  colors.push([
    hexToRgb(colorpicker1.value)["r"],
    hexToRgb(colorpicker1.value)["g"],
    hexToRgb(colorpicker1.value)["b"],
  ]);
  colors.push([
    hexToRgb(colorpicker2.value)["r"],
    hexToRgb(colorpicker2.value)["g"],
    hexToRgb(colorpicker2.value)["b"],
  ]);
  colors.push([
    hexToRgb(colorpicker3.value)["r"],
    hexToRgb(colorpicker3.value)["g"],
    hexToRgb(colorpicker3.value)["b"],
  ]);
  colors.push([
    hexToRgb(colorpicker4.value)["r"],
    hexToRgb(colorpicker4.value)["g"],
    hexToRgb(colorpicker4.value)["b"],
  ]);
  colors.push([
    hexToRgb(colorpicker5.value)["r"],
    hexToRgb(colorpicker5.value)["g"],
    hexToRgb(colorpicker5.value)["b"],
  ]);
  //   let colors = "[";
  //   colors =
  //     colors +
  //     "(" +
  //     hexToRgb(colorpicker1.value)["r"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker1.value)["g"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker1.value)["b"].toString() +
  //     "), ";

  //   colors =
  //     colors +
  //     "(" +
  //     hexToRgb(colorpicker2.value)["r"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker2.value)["g"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker2.value)["b"].toString() +
  //     "), ";

  //   colors =
  //     colors +
  //     "(" +
  //     hexToRgb(colorpicker3.value)["r"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker3.value)["g"].toString() +
  //     ", " +
  //     hexToRgb(colorpicker3.value)["b"].toString() +
  //     ")";

  //   colors =
  //     colors +
  //     "(" +
  //     hexToRgb(colorpicker4.value)["r"].toString() +
  //     "," +
  //     hexToRgb(colorpicker4.value)["g"].toString() +
  //     "," +
  //     hexToRgb(colorpicker4.value)["b"].toString() +
  //     ")";

  //   colors =
  //     colors +
  //     "(" +
  //     hexToRgb(colorpicker5.value)["r"].toString() +
  //     "," +
  //     hexToRgb(colorpicker5.value)["g"].toString() +
  //     "," +
  //     hexToRgb(colorpicker5.value)["b"].toString() +
  //     ")";
  //   colors = colors + "]";
  let data = { colors: colors };

  await postData("http://127.0.0.1:5000/predict", data);
  document.getElementById("result").innerHTML =
    "<img src='./../flask_API/static/images/output.png', class='result-img'/>";
  document.getElementById("result").style.background = "#FFFFFF";
  document.getElementById("result").style.border = "None";
}

async function postData(url = "", data = {}) {
  document.getElementById("result-text").innerHTML = "";
  document.getElementById("loader").style.display = "block";
  const response = await fetch(url, {
    method: "POST",
    mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  document.getElementById("loader").style.display = "none";

  return response; // parses JSON response into native JavaScript objects
}
