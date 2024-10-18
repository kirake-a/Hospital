import { connection } from "./connection.api";
import { Patient } from "../interfaces/patient_interface";

export const createPatient = async (patient_data: Patient) => {
    const response = await connection.post(`patients`, patient_data);
    return response.data;
}

export const getPatientById = async (patient_id: number) => {
    const response = await connection.get(`patients/${patient_id}`);
    return response.data;
}

export const getAllPatients = async () => {
    const response = await connection.get(`patients`);
    return response.data;
}

export const updatePatientById = async (
    patient_id: number,
    patient_data: Patient
) => {
    const response = await connection.put(`patients/${patient_id}`, patient_data);
    return response.data;
}

export const deletePatientById = async (patient_id: number) => {
    const response = await connection.delete(`patients/${patient_id}`);
    return response.data;
}