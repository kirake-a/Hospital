import React, { useState, useEffect } from 'react';
import { Button } from 'primereact/button';
import 'primeicons/primeicons.css';
import { FilterMatchMode } from 'primereact/api';
import { DataTable, DataTableFilterMeta } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { IconField } from 'primereact/iconfield';
import { InputIcon } from 'primereact/inputicon';
//import { Tag } from 'primereact/tag';
//import { CustomerService } from '../service/CustomerService';
import { Patient } from "../interfaces/patient_interface";
import { PatientService } from '../services/PatientService';
//import { getAllPatients, updatePatientById, deletePatientById } from "../api/patients.api";

// interface TableProps {
//     update: boolean;
// }

export default function TablePatients() {
    const [patients, setPatients] = useState<Patient[]>([]);
    const [filters, setFilters] = useState<DataTableFilterMeta>({
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        age: { value: null, matchMode: FilterMatchMode.EQUALS },
        gender: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        tutor_name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        tutor_phone: { value: null, matchMode: FilterMatchMode.STARTS_WITH }
    });
    const [loading, setLoading] = useState<boolean>(true);
    const [globalFilterValue, setGlobalFilterValue] = useState<string>('');

    // const fetchPatients = async () => {
    //     try {
    //         const data = await getAllPatients();
    //         setPatients(data);
    //     } catch (error) {
    //         console.error("Error while fetching patients: ", error);
    //     } finally {
    //         setLoading(false);
    //     }
    // }

    //useEffect(() => {
    //   fetchPatients();
    //}, [update]);

    useEffect(() => {
        PatientService.getPatientsMedium().then((data: Patient[]) => {
            setPatients(getPatients(data));
            setLoading(false);
        });
    }, []);

    const getPatients = (data: Patient[]) => {
        return [...(data || [])].map((d) => {
            // @ts-expect-error Don't know why
            d.birth_date = new Date(d.birth_date);
            // @ts-expect-error Don't know why
            d.registration_date = new Date(d.registration_date);

            return d;
        });
    };

    const onGlobalFilterChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        const _filters = { ...filters };

        // @ts-expect-error Don't know why to write this Table l69
        _filters['global'].value = value;

        setFilters(_filters);
        setGlobalFilterValue(value);
    };

    const renderHeader = () => {
        return (
            <div className="flex justify-content-end">
                <IconField iconPosition="left">
                    <InputIcon className="pi pi-search" />
                    <InputText value={globalFilterValue} onChange={onGlobalFilterChange} placeholder="Finder" />
                </IconField>
            </div>
        );
    };

    const actionBodyTemplate = () => {
        return (
            <div className="flex justify-right gap-2">
                <Button icon="pi pi-eye" severity="success" className="p-2" />
                <Button icon="pi pi-pencil" severity="info" className="p-2" />
                <Button icon="pi pi-trash" severity="danger" className="p-2" onClick={() => confirm("top")} />
            </div>
        );
    };

    const header = renderHeader();

    return (
        <div className="card">
            <DataTable value={patients} paginator rows={10} dataKey="id" filters={filters}  loading={loading}
                    globalFilterFields={['name', 'age', 'gender', 'tutor_name', 'tutor_phone']} header={header}
                    emptyMessage="No patients found.">
                <Column field="name" header="Name" style={{ minWidth: '10rem' }} />
                <Column field="age" header="Age" style={{ minWidth: '10rem' }} />
                <Column field="gender" header="Gender" style={{ minWidth: '10rem' }} />
                <Column field="tutor_name" header="Tutor" style={{ minWidth: '12rem' }} />
                <Column field="tutor_phone" header="Phone" style={{ minWidth: '10rem' }} />
                <Column field="actions" header="Actions" style={{ minWidth: '10rem' }} body={actionBodyTemplate} />
            </DataTable>
        </div>
    );
}
        