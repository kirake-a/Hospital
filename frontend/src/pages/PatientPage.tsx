import { useState } from "react";
import CreatePatientForm from "../components/CreatePatientForm";
import TablePatients from "../components/Table.tsx";


export default function PatientPage() {
    const [updateTable, setUpdateTable] = useState(false);

    const handlePatientCreated = () => {
        setUpdateTable((prev) => !prev);
    };

    return (
        <div>
            <CreatePatientForm onPatientCreated={handlePatientCreated} />
            <TablePatients />
        </div>
      );

}