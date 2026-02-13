function createParticles(count) {
    const geometry = new THREE.BufferGeometry();
    
    // ایجاد آرایه‌ها برای موقعیت و رنگ
    const positions = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);

    function getSphericalDistribution(i) {
        // توزیع یکنواخت نقاط روی کره (Fibonacci Sphere)
        const phi = Math.acos(-1 + (2 * i) / count);
        const theta = Math.sqrt(count * Math.PI) * phi;

        return {
            x: 8 * Math.cos(theta) * Math.sin(phi),
            y: 8 * Math.sin(theta) * Math.sin(phi),
            z: 8 * Math.cos(phi)
        };
    }

    for (let i = 0; i < count; i++) {
        const { x, y, z } = getSphericalDistribution(i);

        // پر کردن آرایه موقعیت (x, y, z)
        positions[i * 3] = x;
        positions[i * 3 + 1] = y;
        positions[i * 3 + 2] = z;

        // پر کردن آرایه رنگ (R, G, B) - به عنوان مثال رنگ سفید
        colors[i * 3] = 1;
        colors[i * 3 + 1] = 1;
        colors[i * 3 + 2] = 1;
    }

    // اضافه کردن ویژگی‌ها به هندسه
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    return geometry;
}