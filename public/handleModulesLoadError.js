// 自定义延时
const delay = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 判断指定的多个模块是否均已加载
const areModulesLoaded = (modules) => {
    return modules.every(module => window[module]);
}

const waitForModules = async () => {
    while (!areModulesDefined(requiredModules)) {
        await delay(100); // 延迟100毫秒
    }

    // 若相关模块均已加载完成，手动初始化DashRenderer
    var renderer = new DashRenderer();
}

const customOnError = async (message, source, lineno, colno, error) => {
    if (message.includes('is not defined') !== -1) {
        await waitForModules();
    }
}

window.onerror = customOnError