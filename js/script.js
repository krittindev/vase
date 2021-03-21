let vase = {
    linedatas: [
      {
        id: 'line1',
        type: 'func',
        legend: 'f(x)',
        color: '#55A8DE',
        visible: true,
        func: func_f,
        dotNum: 1000
      },
      {
        id: 'line2',
        type: 'func',
        legend: 'g(x)',
        color: '#A2CCB6',
        visible: true,
        func: func_g,
        dotNum: 1000
      }
    ],
    config: {
      font: '',
      legendVisible: true,
      title: {
        location: 'center',
        color: '#666666',
        text: 'Vase Equations'
      },
      grid: {
        type: '',
        visible: true,
        color: '#888888'
      },
      border: {
        type: '',
        visible: true,
        color: '#DDDDDD',
        width: 1
      },
      tics: {
        visible: true,
        color: '#888888',
        value: {
          x: 2,
          y: 2
        }
      },
      axis: {
        x: {
          visible: true,
          label: 'X',
          color: '#666666',
          location: 'center',
          range: {
            start: -10,
            end: 10
          }
        },
        y: {
          visible: true,
          label: 'Y',
          color: '#666666',
          location: 'center',
          range: {
            start: -10,
            end: 10
          }
        }
      },
      table: {
        visible: true
      }
    }
  };
let ax = 0,
    ay = 0,
    bx = 0,
    by = 0,
    cx = 0,
    cy = 0,
    dx = 0,
    dy = 0,
    depth = 1,
    coefficient_fx = [],
    coefficient_gx = [],
    volumn = 0;
function calculates(){
    document.getElementById('volumn').innerHTML = "";
    ax = parseFloat(document.getElementById('ax').value);
    ay = parseFloat(document.getElementById('ay').value);
    bx = parseFloat(document.getElementById('bx').value);
    by = parseFloat(document.getElementById('by').value);
    cx = parseFloat(document.getElementById('cx').value);
    cy = parseFloat(document.getElementById('cy').value);
    dx = parseFloat(document.getElementById('dx').value);
    dy = parseFloat(document.getElementById('dy').value);
    depth = parseFloat(document.getElementById('depth').value);
    coefficient_fx.push(    ay/((ax-bx)*(ax-cx)*(ax-dx))
                            +by/((bx-ax)*(bx-cx)*(bx-dx))
                            +cy/((cx-bx)*(cx-ax)*(cx-dx))
                            +dy/((dx-bx)*(dx-cx)*(dx-ax))
    );
    coefficient_fx.push(    ay*(-(bx+cx+dx))/((ax-bx)*(ax-cx)*(ax-dx))
                            +by*(-(ax+cx+dx))/((bx-ax)*(bx-cx)*(bx-dx))
                            +cy*(-(ax+bx+dx))/((cx-bx)*(cx-ax)*(cx-dx))
                            +dy*(-(ax+bx+cx))/((dx-bx)*(dx-cx)*(dx-ax))
    );
    coefficient_fx.push(   (ay*(bx+cx+dx)/((ax-bx)*(ax-cx)*(ax-dx))
                            -by*(ax+cx+dx)/((bx-ax)*(bx-cx)*(bx-dx))
                            +cy*(ax+bx+dx)/((cx-bx)*(cx-ax)*(cx-dx))
                            -dy*(ax+bx+cx)/((dx-bx)*(dx-cx)*(dx-ax)))*-1
    );
    coefficient_fx.push(   (ay*(bx*cx*dx)/((ax-bx)*(ax-cx)*(ax-dx))
                            +by*(ax*cx*dx)/((bx-ax)*(bx-cx)*(bx-dx))
                            +cy*(ax*bx*dx)/((cx-bx)*(cx-ax)*(cx-dx))
                            +dy*(ax*bx*cx)/((dx-bx)*(dx-cx)*(dx-ax)))*-1 
    );
    coefficient_gx = [...coefficient_fx];
    coefficient_gx[3] -= depth;
    volumn = (integral_f(dx) - integral_f(ax)) - (integral_g(dx) - integral_g(ax)) + integral_g(depth);
    document.getElementById('volumn').innerHTML = parseInt(volumn * (10 ** 2)) / (10 ** 2);

    console.log("ax: ",ax);
    console.log("ay: ",ay);
    console.log("bx: ",bx);
    console.log("by: ",by);
    console.log("cx: ",cx);
    console.log("cy: ",cy);
    console.log("dx: ",dx);
    console.log("dy: ",dy);
    console.log("depth: ",depth);
    console.log("coefficient_fx: ",coefficient_fx);
    console.log("coefficient_gx: ",coefficient_gx);
    console.log("volumn: ",volumn);

    
    plotta.UpdateGraph(vase);
}

function func_f(x){
    // console.log(coefficient_fx[0],"x^3+",coefficient_fx[1],"x^2+",coefficient_fx[2],"x+",coefficient_fx[3]);
    return coefficient_fx[0]*x**3 + coefficient_fx[1]*x**2 + coefficient_fx[2]*x + coefficient_fx[3]
}
function func_g(x){
    // console.log(coefficient_gx[0],"x^3+",coefficient_gx[1],"x^2+",coefficient_gx[2],"x+",coefficient_gx[3]);
    return coefficient_gx[0]*x**3 + coefficient_gx[1]*x**2 + coefficient_gx[2]*x + coefficient_gx[3]
}
function integral_f(x){
    return (22 / 7) * ((((coefficient_fx[0] ** 2) * (x ** 7)) / 7)
         + ((1 / 3) * (x ** 6) * (coefficient_fx[0] * coefficient_fx[1]))
         + ((1 / 5) * (x ** 5) * (2 * (coefficient_fx[0] * coefficient_fx[2]) + (coefficient_fx[1] ** 2)))
         + ((1 / 2) * (x ** 4) * ((coefficient_fx[0] * coefficient_fx[3]) + (coefficient_fx[1] * coefficient_fx[2])))
         + ((1 / 3) * (x ** 3) * (2 * (coefficient_fx[1] * coefficient_fx[3]) + (coefficient_fx[2] ** 2)))
         + (coefficient_fx[2] * coefficient_fx[3] * (x ** 2))
         + ((coefficient_fx[3] ** 2) * x))
}
function integral_g(x){
    return (22 / 7) * ((((coefficient_gx[0] ** 2) * (x ** 7)) / 7)
         + ((1 / 3) * (x ** 6) * (coefficient_gx[0] * coefficient_gx[1]))
         + ((1 / 5) * (x ** 5) * (2 * (coefficient_gx[0] * coefficient_gx[2]) + (coefficient_gx[1] ** 2)))
         + ((1 / 2) * (x ** 4) * ((coefficient_gx[0] * coefficient_gx[3]) + (coefficient_gx[1] * coefficient_gx[2])))
         + ((1 / 3) * (x ** 3) * (2 * (coefficient_gx[1] * coefficient_gx[3]) + (coefficient_gx[2] ** 2)))
         + (coefficient_gx[2] * coefficient_gx[3] * (x ** 2))
         + ((coefficient_gx[3] ** 2) * x))
}
