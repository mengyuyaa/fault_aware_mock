// 使用 Mock
let Random = Mock.Random;
var data = Mock.mock({
    // 属性 list 的值是一个数组，其中含有 1 到 10 个元素
    'list|1-50': [{
        // 属性 id 是一个自增数，起始值为 1，每次增 1
        'id|+1': 1,
        "fault_type|1-15": 1,
        "create_time": Random.datetime("2021-MM-dd HH:mm:ss"),
        "host_id|1-10000": 1,
        "server_product_id|1-10": 1,
        "fw_bios|1-10": 1,
        "idc|1-10": 1,
        "devicespec_id|1-10": 1 
    }]
})
// 输出结果
console.log(JSON.stringify(data, null, 4))
// Mock.toJSONSchema(data)