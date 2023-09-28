var scene, renderer
var camera, controls

var spotlight

var cube = []
var empty_cube = []

var separatorLength = 3

function init() {
    scene = new THREE.Scene()

    var axis = new THREE.AxisHelper(20)
    scene.add(axis)

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    camera.position.set(15, 15, 15)

    renderer = new THREE.WebGLRenderer()
    renderer.setClearColor(new THREE.Color(0xEEEEEE, 1.0))
    renderer.setSize(window.innerWidth, window.innerHeight)
    renderer.shadowMapEnabled = true
    document.body.appendChild(renderer.domElement)

    spotlight = new THREE.SpotLight(0xffffff)
    spotlight.position.set(10, 10, 10)
    spotlight.castShadow = true
    scene.add(spotlight)

    controls = new THREE.OrbitControls(camera, renderer.domElement)
    controls.userPan = false
    camera.lookAt(0, 0, 0)
    controls.update()

    controls.addEventListener('change', () => console.log("Controls Change"))
    controls.addEventListener('start', () => console.log("Controls Start Event"))
    controls.addEventListener('end', () => console.log("Controls End Event"))

    controls.dampingFactor = .01

    controls.minAzimuthAngle = 0
    controls.maxAzimuthAngle = Math.PI / 2

    controls.minPolarAngle = 0
    controls.maxPolarAngle = Math.PI

    controls.maxDistance = 15
    controls.minDistance = 5

    cube.push(createCube(0, 0, 0, 2, 0xffffff, true))
    cube.push(createCube(0, 3, 0, 2, 0xffffff, true))
    cube.push(createCube(0, -3, 0, 2, 0xffffff, true))

    empty_cube = cube

    for(let i = 0; i < cube.size; i++) {
        scene.add(cube[i])
    }

    window.addEventListener('resize', resize, false)
}   

function resize() {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    render()
}

function animate() {
    requestAnimationFrame(animate)
    controls.update()

    render()
}

function render() {
    renderer.render(scene, camera)
}

function createCube(x, y, z, size, color, shadow) {
    var geometry = new THREE.BoxGeometry(size, size, size);
    var material = new THREE.MeshLambertMaterial({color: 0xcccccc});
    var cube = new THREE.Mesh(geometry, material);

    cube.position.set(x, y, z)
    cube.castShadow = true;

    scene.add(cube);
    return cube
}

function createPart(size) {
    
}

function near(x, y, z) {
    var nearX1 = x + separatorLength
    var nearX2 = x - separatorLength

    var nearY1 = y + separatorLength
    var nearY2 = y - separatorLength

    var nearZ1 = z + separatorLength
    var nearZ2 = z - separatorLength

    for(let i = 0; i < cube.size; i++) {
        if(nearX1 == cube[i].position.x) {
            
        }
    }
}

window.onload = init;
animate()
