from develop.utils import load_data, get_executed_operations, get_operations_with_from, get_last_five_operations
from operation_class import Operation


def main():
    filename = "develop/operations.json"
    data = load_data(filename)
    executed_operations = get_executed_operations(data)
    operations_with_from = get_operations_with_from(executed_operations)
    last_five_operations = get_last_five_operations(operations_with_from, 5)

    operations = [
        Operation(
            operation_data.get("id", None),
            operation_data.get("state", ""),
            operation_data.get("date", ""),
            operation_data.get("operationAmount", {}),
            operation_data.get("description", ""),
            operation_data.get("from", ""),
            operation_data.get("to", "")
        )
        for operation_data in last_five_operations
    ]

    for operation in operations:
        print(operation)


if __name__ == "__main__":
    main()
